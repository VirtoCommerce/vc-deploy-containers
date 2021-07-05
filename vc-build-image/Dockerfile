FROM mcr.microsoft.com/dotnet/sdk:3.1

RUN dotnet tool install -g virtocommerce.globaltool \
    && export PATH="$PATH:/root/.dotnet/tools"

ENTRYPOINT [ "/root/.dotnet/tools/vc-build", "install" ]

#For conatainerd1