storage "mysql" {
    address  = "10.0.0.6:3306"
    username = "trace"
    password = "trace"
    database = "vault_db"
    }

listener "tcp" {
    address     = "0.0.0.0:8200"
    tls_cert_file = "/home/trace/vault/vault.crt"
    tls_key_file  = "/home/trace/vault/vault.key"
}

api_addr = "https://vault.tracecloud.click:8200"
cluster_addr = "https://127.0.0.1:8201"
ui = true