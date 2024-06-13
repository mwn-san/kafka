# CHEAT SHEET

Verify SSL Certificate The Keystore and Truststore
```
keytool --lis -v --keystore filename.jks
keytool --lis -v --keystore filename.jks | grep Valid
keytool --lis -v --keystore filename.jks | grep Alias
keytool --lis -v --keystore filename.jks | grep Serial
```
Converting a Java Keystore (.JKS) to (.PEM) File format
```
NOTE: 
  By default, the JKS key store type doesn't support exporting the Private key entry using the key tool
  Private key entry can be exported by converting the JKS to a PKCS12 key store
  Command for converting JKS to PKCS12 key store can be found in step 1 on script
  We will use the PKCS12 key store 'sample_keystore.pfx' and export the private key entry in 'PEM' format using the following OpenSSL command
  Options:
          -nodes: No DES format so the Private key won't be encrypted
          -nocerts: No certificates will be exported at all, only the private key entry
```

Certificate checker --> https://www.sslshopper.com/certificate-key-matcher.html
