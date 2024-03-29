mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS=false\n\
enableWebsocketCompression=false\n\
enableXsrfProtection=false\n\
" > ~/.streamlit/config.toml
