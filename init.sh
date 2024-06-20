init_components() {
    echo "Initializing components..."
    check_ollama
    check_docker
    # run containers by docker-compose
    docker-compose up -d  
    echo "Components initialized."
    # run llama3 by ollama
    ollama run llama3 
}

# check ollama is installed
check_ollama() {
if ! [ -x "$(command -v ollama)" ]; then
    echo "Error: ollama is not installed." >&2
    exit 1
fi
}

# check docker is installed
check_docker() {
if ! [ -x "$(command -v docker)" ]; then
    echo "Error: docker is not installed." >&2
    exit 1
fi
}


init_components