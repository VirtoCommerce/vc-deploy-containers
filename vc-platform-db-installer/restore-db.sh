#!/bin/bash
mkdir ./downloads
wget -q "$1" -O ./downloads/db.bacpac
/opt/mssql-tools/sqlpackage/sqlpackage /Action:Import /TargetServerName:"$2" /TargetUser:"$3" /TargetPassword:"$4" /TargetDatabaseName:"$5" /SourceFile:"./downloads/db.bacpac"
rm -r ./downloads