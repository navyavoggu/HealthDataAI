import requests
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="HealthData AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 HealthData AI")
st.subheader("Healthcare Data Intelligence Dashboard")
st.write(
    "Explore provider information, filter records, "
    "visualize data, and download reports."
)

# Fictional sample data for demonstration
data = pd.DataFrame({
    "Provider": [
        "City Care Clinic",
        "Green Life Hospital",
        "Sunrise Medical Center",
        "Wellness Family Clinic",
        "Metro Health Center",
        "Hope Medical Clinic",
        "Care Plus Hospital",
        "Family Health Center"
    ],
    "Specialty": [
        "General Medicine",
        "Cardiology",
        "Pediatrics",
        "General Medicine",
        "Cardiology",
        "Dermatology",
        "Pediatrics",
        "Dermatology"
    ],
    "City": [
        "Hyderabad",
        "Bengaluru",
        "Hyderabad",
        "Chennai",
        "Bengaluru",
        "Hyderabad",
        "Chennai",
        "Bengaluru"
    ]
})

st.caption(
    "Demo dataset: all provider names are fictional."
)

st.sidebar.header("Search and Filters")

search = st.sidebar.text_input("Search provider name")

specialties = ["All"] + sorted(
    data["Specialty"].unique().tolist()
)
cities = ["All"] + sorted(data["City"].unique().tolist())

specialty = st.sidebar.selectbox(
    "Specialty", specialties
)
city = st.sidebar.selectbox("City", cities)

filtered = data.copy()

if search.strip():
    filtered = filtered[
        filtered["Provider"].str.contains(
            search.strip(), case=False, na=False
        )
    ]

if specialty != "All":
    filtered = filtered[
        filtered["Specialty"] == specialty
    ]

if city != "All":
    filtered = filtered[filtered["City"] == city]

col1, col2, col3 = st.columns(3)

col1.metric("Total providers", len(filtered))
col2.metric("Cities represented", filtered["City"].nunique())
col3.metric("Specialties", filtered["Specialty"].nunique())

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Provider Directory")
    st.dataframe(filtered, use_container_width=True)

with right:
    st.subheader("Providers by Specialty")

    counts = filtered["Specialty"].value_counts().reset_index()
    counts.columns = ["Specialty", "Count"]

    if not counts.empty:
        fig = px.bar(
            counts,
            x="Specialty",
            y="Count",
            text="Count",
            title="Distribution of Providers"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No records match your filters.")

st.subheader("Data Export")

st.download_button(
    label="Download filtered records (CSV)",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="healthcare_providers.csv",
    mime="text/csv"
)

st.info(
    "Next enhancement: add an AI-generated summary "
    "of the filtered data."
)




st.divider()

st.header("📊 Smart Data Insights")
st.caption("Automatic analysis of the currently filtered records")

if filtered.empty:
    st.warning("No records available to analyze.")
else:
    city_counts = filtered["City"].value_counts()
    specialty_counts = filtered["Specialty"].value_counts()

    st.subheader("Key Findings")

    if not city_counts.empty:
        st.write(
            f"• Most represented city: **{city_counts.index[0]}** "
            f"({city_counts.iloc[0]} providers)"
        )

    if not specialty_counts.empty:
        st.write(
            f"• Most represented specialty: "
            f"**{specialty_counts.index[0]}** "
            f"({specialty_counts.iloc[0]} providers)"
        )

    st.write(
        f"• The current selection contains {len(filtered)} "
        f"provider records across {filtered['City'].nunique()} "
        f"cities and {filtered['Specialty'].nunique()} specialties."
    )

    st.caption(
        "These are rule-based insights calculated from the demo data, "
        "not AI-generated medical advice."
    )

st.divider()
st.header("🤖 AI-Powered Summary")
st.write("Generate a summary using your local Ollama model.")

if st.button("Generate AI Summary"):
    if filtered.empty:
        st.warning("No provider records available to summarize.")
    else:
        records = filtered[
            ["Provider", "Specialty", "City"]
        ].to_dict(orient="records")

        
        city_counts = filtered["City"].value_counts().to_dict()
        specialty_counts = filtered["Specialty"].value_counts().to_dict()

        prompt = f"""
        You are a careful data analyst.

        Analyze these fictional healthcare provider records:
        {records}

        Verified statistics calculated by Python:
        Total providers: {len(filtered)}
        Number of cities: {filtered["City"].nunique()}
        Number of specialties: {filtered["Specialty"].nunique()}
        Providers by city: {city_counts}
        Providers by specialty: {specialty_counts}

        Write a concise report containing:
        1. A one-sentence summary.
        2. The most represented city and its exact count.
        3. The most represented specialty and its exact count.
        4. One observation based only on the supplied data.

        Use only the verified statistics above.
        Do not change, guess, or invent any counts.
        If multiple categories are tied, mention the tie.
        Do not provide medical advice.
        """


        try:
            with st.spinner("Generating AI summary..."):
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "llama3.2:1b",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=180
                )

                response.raise_for_status()
                result = response.json()

            st.markdown(result["response"])

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to Ollama. "
                "Make sure Ollama is running on this computer."
            )
        except requests.exceptions.Timeout:
            st.error("The AI took too long to respond. Please try again.")
        except requests.exceptions.RequestException as error:
            st.error(f"AI request failed: {error}")
        except (ValueError, KeyError):
            st.error("Could not read the AI response. Please try again.")
