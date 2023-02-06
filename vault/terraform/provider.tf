terraform {
  required_providers {
    vault = {
      source = "hashicorp/vault"
      version = "3.12.0"
    }
  }
}

provider "vault" {
    address = "vault.tracecloud.click:8200"
    token = ""
}



