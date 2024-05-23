# Create a Wildcard SSL certificate from File
This project is used to create wildcard SSL certificates from proprietary files

# Getting Started
Certificate files owned:
```bash
TrustedRoot.crt
DigiCertCA2.crt
domain.crt
domain.key
```
Generate ca_bundle.pem, make sure private key file "domain.key" WITHOUT PASSWORD
```bash
export PASS=pegadaian
cat domain.crt DigiCertCA2.crt TrustedRoot.crt > ca_bundle.pem
```
Generate Truststore
```bash
keytool -keystore domain.com.truststore.jks -alias CARoot -import -file TrustedRoot.cer -storepass $PASS -keypass $PASS
```
Generate Keystore
```bash
openssl pkcs12 -export -name domain.com -in ca_bundle.pem -inkey domain.key -out domain.com.p12 -passout pass:$PASS
```
Import Key
```bash
keytool -importkeystore -destkeystore domain.com.keystore.jks -srckeystore domain.com.p12 -srcstoretype pkcs12 -alias domain.com -srcstorepass $PASS -deststorepass $PASS -destkeypass $PASS
```
Verify file (.JKS) Keystore and Truststore:
```bash
keytool -list -v -keystore domain.com.truststore.jks -storepass $PASS -keypass $PASS | grep Valid
keytool -list -v -keystore domain.com.keystore.jks -storepass $PASS -keypass $PASS | grep Serial
```
Note:
# <p align="center"> 𝗠𝗔𝗞𝗘 𝗦𝗨𝗥𝗘 𝗦𝗘𝗥𝗜𝗔𝗟 𝗢𝗡 𝗞𝗘𝗬𝗦𝗧𝗢𝗥𝗘 𝗔𝗡𝗗 𝗧𝗥𝗨𝗦𝗧𝗦𝗧𝗢𝗥𝗘 </p>
```bash
keytool --list -v --keystore domain.com.keystore.jks -keypass $PASS | grep Serial
# result :
Serial number: 87835d2e3062f63d
Serial number: 9d5561ff327a5036
```
```bash
keytool --list -v --keystore domain.com.truststore.jks -keypass $PASS | grep Serial
# result
Serial number: 9d5561ff327a5036
```
