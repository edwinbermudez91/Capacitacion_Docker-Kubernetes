# Ejercicio: Despliegue Stateless (Aplicación Web con ConfigMap)

**Objetivo:** Aprender a desplegar una aplicación web sin estado (stateless), inyectando configuración de entorno mediante **ConfigMaps** y exponiéndola al exterior con un **Service**.

En este ejercicio utilizaremos los manifiestos que se encuentran en la carpeta `stateless/`:
- `configmap.yaml`: Define variables de configuración, como el color de fondo de la aplicación (`APP_COLOR: "blue"`).
- `deployment.yaml`: Despliega múltiples réplicas (Pods) de la aplicación web asegurando que siempre estén disponibles. Lee los valores del ConfigMap.
- `service.yaml`: Expone los Pods mediante un puerto accesible desde fuera del clúster (NodePort).

## 1. Desplegar los recursos

Ubícate en la carpeta `laboratorios/lab2-kubernetes/` y aplica todos los manifiestos de la carpeta `stateless/` de forma simultánea:

```bash
kubectl apply -f stateless/
```

## 2. Verificar el despliegue

Comprueba que los Pods, el ConfigMap y el Service estén activos:

```bash
kubectl get pods,svc,configmap
kubectl exec -it deployment/color-app -- env | grep APP_COLOR   # Debería mostrar APP_COLOR=blue
```

## 3. Acceder a la aplicación en el navegador

Dependiendo de tu entorno de Kubernetes, puedes abrir la aplicación web con cualquiera de estas dos opciones:

- **Opción A — Usando Port-Forward (funciona en cualquier clúster: kind, Minikube, Docker Desktop, iximiuz Labs):**
  ```bash
  kubectl port-forward svc/color-svc 8080:80
  ```
  Luego abre en tu navegador: `http://localhost:8080`

- **Opción B — Usando NodePort en Minikube:**
  ```bash
  minikube service color-svc --url
  ```

## 4. Experimentar: Cambiar el color dinámicamente con ConfigMap

Edita el archivo `stateless/configmap.yaml` (o usa `kubectl patch`) para cambiar el color de `"blue"` a `"green"`, `"red"` o `"pink"` y reinicia los Pods del Deployment para que tomen el nuevo valor:

```bash
kubectl patch configmap app-config -p '{"data":{"APP_COLOR":"green"}}'
kubectl rollout restart deployment/color-app
kubectl rollout status deployment/color-app
```

Recarga tu navegador en `http://localhost:8080` y verás el nuevo color aplicado sin haber modificado la imagen del contenedor.

## 5. Limpieza

```bash
kubectl delete -f stateless/
```
