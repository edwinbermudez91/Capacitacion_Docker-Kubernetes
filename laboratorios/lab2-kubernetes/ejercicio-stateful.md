# Ejercicio: Despliegue Stateful (Base de Datos y Frontend)

**Objetivo:** Aprender a gestionar datos sensibles con **Secrets**, desplegar bases de datos usando **StatefulSets** y conectar aplicaciones usando **Deployments**.

En este ejercicio utilizaremos los manifiestos de la carpeta actual:
- `secret.yaml`: Contiene las credenciales de la base de datos de forma segura.
- `statefulset-db.yaml`: Despliega un clúster MySQL (1 réplica) y un servicio *Headless*.
- `frontend.yaml`: Despliega la aplicación `Adminer` para administrar la base de datos visualmente.

## 1. Desplegar los recursos

Aplica los manifiestos en tu clúster de Kubernetes ejecutando:

```bash
kubectl apply -f secret.yaml
kubectl apply -f statefulset-db.yaml
kubectl apply -f frontend.yaml
```

## 2. Verificar el despliegue

Revisa que los pods, el statefulset, los servicios y los secretos se hayan creado y estén en ejecución:

```bash
kubectl get statefulset,pods,svc,secrets
```

## 3. Probar la conexión a la base de datos

1. Identifica el puerto expuesto para el servicio `frontend-svc`. En la salida del comando anterior, busca la columna `PORT(S)`. Verás algo como `80:3XXXX/TCP`. El puerto NodePort asignado es el `3XXXX`.
2. Abre tu navegador web y accede a `http://<IP-NODO>:<PUERTO-NODEPORT>`. 
   * *Nota: Si estás usando **Minikube**, puedes obtener la URL exacta directamente ejecutando `minikube service frontend-svc --url`.*
3. En la pantalla de login de **Adminer**, introduce las credenciales exactas que se definieron en el Secret:
   * **Motor:** `MySQL`
   * **Servidor:** `mysql-headless` *(este es el nombre DNS del servicio asociado al StatefulSet)*
   * **Usuario:** `dbuser`
   * **Contraseña:** `dbpassword123`
   * **Base de datos:** `testdb`

Al dar clic en "Entrar", deberías ver la interfaz de administración de la base de datos. ¡Esto confirma que tu Frontend (Deployment) logró resolver el nombre del servicio y conectarse al backend (StatefulSet)!

## 4. Limpieza de recursos

Una vez finalizado el laboratorio, elimina los recursos para liberar espacio en tu clúster:

```bash
kubectl delete -f frontend.yaml
kubectl delete -f statefulset-db.yaml
kubectl delete -f secret.yaml
```