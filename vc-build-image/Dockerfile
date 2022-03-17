#Install virtocommerce.globaltool
FROM mcr.microsoft.com/dotnet/sdk:6.0

RUN dotnet tool install -g virtocommerce.globaltool

ENV PATH="/root/.dotnet/tools:${PATH}"

CMD [ "vc-build", "install" ]