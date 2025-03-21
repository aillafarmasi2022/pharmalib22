import streamlit as st

st.title("Aplikasi Farmasi")
st.write("Selamat datang di aplikasi berbasis Streamlit!")

nama = st.text_input("Masukkan Nama Anda:")
if nama:
    st.write(f"Halo, {nama}!")

data = {
    "Istilah Latin": ["Aqua", "Extractum", "Pulvis", "Tinctura", "Unguentum"],
    "Terjemahan": ["Air", "Ekstrak", "Serbuk", "Tingtur", "Salep"]
}
df = pd.DataFrame(data)

@app.route('/')
def index():
    return render_template('index.html', data=df.to_dict(orient='records'))

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').lower()
    results = df[df["Istilah Latin"].str.lower().str.contains(query, na=False)]
    return render_template('index.html', data=results.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
