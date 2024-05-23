#!/bin/bash

# === created by mohammad wildan nuryulda (nuryulda@gmail.com) === #

# Set the list of domain names
domains=("your-domain.com")

# Iterate over each domain
for domain in "${domains[@]}"; do
    # 1. Converting a JKS to PKCS12 keystore
    #---------------------------------------#
    keytool -importkeystore -srckeystore "${domain}.keystore.jks" -destkeystore "${domain}.pfx" -deststoretype pkcs12

    sleep 5  # Pause for 5 seconds

    # 2. Export public certificate from JKS in DER format (binary-encoded format)
    #----------------------------------------------------------------------------#
    keytool -exportcert -alias "${domain}" -file "${domain}.crt" -keystore "${domain}.keystore.jks"

    sleep 5  # Pause for 5 seconds

    # 3. Export public certificate from JKS in PEM format (ASCII Base64 human-readable format)
    #----------------------------------------------------------------------------------------#
    # Additional '-rfc' option needs to be passed along with '-exportcert' option to get a PEM encoded certificate
    keytool -exportcert -alias "${domain}" -file "${domain}.pem" -keystore "${domain}.keystore.jks" -rfc

    sleep 5  # Pause for 5 seconds

    # 4. Export private key entry from JKS
    #-------------------------------------#
    # By default, the JKS key store type doesn't support exporting the Private key entry using the key tool
    # Private key entry can be exported by converting the JKS to a PKCS12 key store
    # Command for converting JKS to PKCS12 key store can be found in 1
    # We will use the PKCS12 key store '${domain}.pfx' and export the private key entry in 'PEM' format using the following OpenSSL command
    # Options:
    #       -nodes: No DES format so the Private key won't be encrypted
    #       -nocerts: No certificates will be exported at all, only the private key entry
    openssl pkcs12 -in "${domain}.pfx" -nodes -nocerts -out "${domain}.private.key.pem"

    sleep 5  # Pause for 5 seconds
done


