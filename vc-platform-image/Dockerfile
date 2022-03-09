FROM ghcr.io/virtocommerce/vc-deploy-containers/vc-build-image:stable as build

WORKDIR /platform

COPY vc-package.json /platform 

RUN /root/.dotnet/tools/vc-build install -SkipDependencySolving && /root/.dotnet/tools/vc-build initplatform

FROM mcr.microsoft.com/dotnet/aspnet:6.0-alpine

COPY --from=build platform /opt/virtocommerce/platform
COPY YamlDotNet.dll /opt/virtocommerce/platform/app_data/modules

RUN apt-get update && apt-get install -y wget fontconfig libfreetype6 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base libjpeg62-turbo \
    && wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb && dpkg -i wkhtmltox_0.12.6-1.buster_amd64.deb

WORKDIR /opt/virtocommerce/platform

ENTRYPOINT ["dotnet", "VirtoCommerce.Platform.Web.dll"]

#For containerd in k8s cluster!!