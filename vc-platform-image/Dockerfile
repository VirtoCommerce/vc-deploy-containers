FROM docker.pkg.github.com/virtocommerce/vc-deploy-containers/vc-build-image:stable as build

RUN mkdir /platform

COPY vc-package.json /platform 

RUN cd /platform && /root/.dotnet/tools/vc-build install -SkipDependencySolving && /root/.dotnet/tools/vc-build initplatform

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1

COPY --from=build platform /opt/virtocommerce/platform

RUN apt-get update && apt-get install -y wget fontconfig libfreetype6 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base libjpeg62-turbo \
    && wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb && dpkg -i wkhtmltox_0.12.6-1.buster_amd64.deb

WORKDIR /opt/virtocommerce/platform

ENTRYPOINT ["dotnet", "VirtoCommerce.Platform.Web.dll"]