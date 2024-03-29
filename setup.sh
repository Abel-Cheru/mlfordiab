mkdir -p ~/.streamlit/

echo "
[general]
email = \"email@domain\
" > ~/.streamlit/credentials.toml

echo "
[server]
headless = true
port = $PORT
enableCORS=false
" > ~/.streamlit/config.toml
