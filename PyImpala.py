import pyodbc

connection_string = '''DRIVER={Cloudera ODBC Driver for Impala};
UseSystemTrustStore=0;
UseSQLUnicodeTypes=0;
UseSASL=<1 or 0>;
UseOnlySSPI=0;
UseNativeQuery=0;
UseKeytab=0;
TSaslTransportBufSize=<Refer your ODBC System DSN>;
TrustedCerts=<Path for tursted certificate>;
StringColumnLength=<Refer your ODBC System DSN>;
SSL=<1 or 0>;
SocketTimeout=<Socket Timeout from ODBC System DSN>;
RowsFetchedPerBlock=<Defaults from ODBC System DSN>;
Port=<port # ODBC System DSN>;
KrbServiceName=<Kerberos Service Name is using Kerberos authentication implemented on your cluster>;
KrbRealm=<Refer your ODBC System DSN>;
KrbFQDN=<Refer your ODBC System DSN>;
Host=<Refer your ODBC System DSN>;
EnableSimulatedTransactions=0;
DelegateKrbCreds=0;
AutoReconnect=1;
AuthMech=1;
AllowSelfSignedServerCert=0;
AllowHostNameCNMismatch=0'''

connection = pyodbc.connect(connection_string, autocommit=True)
cursor = connection.cursor()

#Reading Data from an existing Impala Table

for row in cursor.execute('select [Col-Name] from [Table-name]'):
	print(row.[Col-Name]...)
