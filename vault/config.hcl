storage "mysql" {
    username = "vault"
    password = "vault-secret-key"
    database = "vault_db"
    address  = "10.0.0.14:3306"
}



listener "tcp" {
    address     = "vault.tracecloud.click:8200"
    tls_cert_file = "/opt/vault/tls/vault.crt"
    tls_key_file  = "/opt/vault/tls/vault.key"

}

api_addr = "https://vault.tracecloud.click:8200"
cluster_addr = "https://127.0.0.1:8201"
ui = true
