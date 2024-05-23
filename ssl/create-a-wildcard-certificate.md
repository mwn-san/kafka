#  Create Wildcard SSL Certificate for Development Environment
This project is used to create your own wildcard SSL certificate for development environment,

created by MWN nuryulda@gmail.com and hopefully it can be useful and helpful.
# Getting started

Create Private Key for CA:
```bash
openssl genrsa -out ca.key 2048
```
Create Root Certificate (self-signed):
```bash
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1024 -out ca.pem -subj "/C=ID/ST=Jakarta/L=Jakarta/O=Example Security/OU=CA/CN=Example Root CA"
```
Create Private Key for Sertifikat:
```bash
openssl genrsa -out example.co.id.key 2048
```
Create Certificate Signing Request (CSR):
```bash
openssl req -new -key example.co.id.key -out example.co.id.csr -subj "/C=ID/ST=Jakarta/L=Jakarta/O=Example Security/OU=IT/CN=*.example.co.id"
```
Create Config file for Certificate Extension with name the example.ext:
```bash
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = *.example.co.id
DNS.2 = example.co.id
```
Sign the CSR with the CA (or skip this step if using an external CA):
```bash
openssl x509 -req -in example.co.id.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out example.co.id.crt -days 500 -sha256 -extfile example.ext
```
Importing CA and wildcard certificates into the keystore:
```bash
openssl pkcs12 -export -in example.co.id.crt -inkey example.co.id.key -out example.co.id.p12 -name example.co.id -CAfile ca.pem -caname root -chain
```
Then, import PKCS#12 into the keystore (JKS format):
```bash
keytool -importkeystore -deststorepass confluent -destkeypass confluent -destkeystore example.co.id.keystore.jks -srckeystore example.co.id.p12 -srcstoretype PKCS12 -srcstorepass confluent -alias example.co.id
```
Import CA ke truststore:
```bash
keytool -import -file ca.pem -alias rootCA -keystore example.co.id.truststore.jks -storepass confluent
```
Verify file (.JKS) Keystore and Truststore:
```bash
keytool -list -v -keystore example.co.id.truststore.jks -storepass $PASS -keypass $PASS | grep Valid
keytool -list -v -keystore example.co.id.keystore.jks -storepass $PASS -keypass $PASS | grep Serial
```
Note:
# <p align="center"> 𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗦𝗘𝗥𝗜𝗔𝗟 𝗢𝗡 𝗞𝗘𝗬𝗦𝗧𝗢𝗥𝗘 𝗔𝗡𝗗 𝗧𝗥𝗨𝗦𝗧𝗦𝗧𝗢𝗥𝗘 </p>
```bash
keytool --list -v --keystore example.co.id.keystore.jks -keypass $PASS | grep Serial
# result :
Serial number: 87835d2e3062f63d
Serial number: 9d5561ff327a5036
```
```bash
keytool --list -v --keystore example.co.id.truststore.jks -keypass $PASS | grep Serial
# result
Serial number: 9d5561ff327a5036
```


