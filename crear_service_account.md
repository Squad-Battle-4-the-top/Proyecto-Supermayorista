# Service Account

## Pasos para crear una service account

<p align="justify">
1. En Google Cloud Platform (GCP), seleccione el ícono de hamburguesa, luego seleccione IAM &Admin, y finalmente haga clic en Service Accounts
</p>

<p align="center">
  <img src="Imagenes\IAM_sien_project.png">
</p>

<p align="justify">
2. Click en <code>+CREATE SERVICE ACCOUNT</code>
</p>
<p align="center">
  <img src="Imagenes\create_service_account.png">
</p>
<p align="justify">
3. Elige el nombre de tu service account. Elegí como nombre de cuenta de servicio: terraform-sien
</p>
<p align="center">
  <img src="Imagenes\terraform-sien.png">
</p>
<p align="justify">
4. Asigne el rol de viewer por ahora y haga clic en <code>DONE</code>
</P>

<p align="center">
  <img src="Imagenes\service_basic_viewer.png">
</p>
<p align="justify">
5.  Necesitamos acceder a esta cuenta de servicio mediante la CLI de Google Cloud, para eso genere un <CODE>Manage keys</CODE> y elegir el archivo JSON.
</p>
<p align="center">
  <img src="Imagenes\generate_key_service_account.png">
</p>

<p align="justify">
6. Guarde el archivo en la siguiente ruta 
</p>

    cd 
    mkdir .gc

<p align="center">
  <img src="Imagenes\gc_file_json.png">
</p>

<p align="justify">
7. Autenticarse con Google Cloud SDK

    export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/sien-project.json
    gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS

<p align="center">
  <img src="Imagenes\export_google_credentials.png">
</p>
<p align="justify">
8. Añadamos más servicios para Big Query Admin,seleccione el ícono de hamburguesa, luego seleccione IAM &Admin, y finalmente haga clic en IAM
</p>

<p align="center">
  <img src="Imagenes\iam.png">
</p>

Click en <code>Edit Principal</code>

<p align="center">
  <img src="Imagenes\edit_permissions_terraform_sien.png">
</p>

Click en <code>+ ADD ANOHTER ROLE</code> añadir el Rol de BigQuery Admiin y click en <code>SAVE</code> :
<p align="center">
  <img src="Imagenes\more_premissions_terraform.png">
</p>

<p align="justify">
9. Activar dos APIs.
</p>


- Identity and Access Management (IAM) API
- IAM Service Account Credentials API

<p align="center">
  <img src="Imagenes\IAM_API.png">
</p>

<p align="center">
  <img src="Imagenes\IAM_API_2.png">
</p>