# Ejercicio: Despliegue Stateless (Aplicación Web con ConfigMap)

**Objetivo:** Aprender a desplegar una aplicación web sin estado (stateless), inyectando configuración de entorno mediante **ConfigMaps** y exponiéndola al exterior con un **Service**.

En este ejercicio utilizaremos los manifiestos que se encuentran en la carpeta `stateless/`:
- `configmap.yaml`: Define variables de configuración, como el color de fondo de la aplicación (`APP_COLOR: "blue"`).
- `deployment.yaml`: Despliega múltiples réplicas (Pods) de la aplicación web asegurando que siempre estén disponibles. Lee los valores del ConfigMap.
- `service.yaml`: Expone los Pods mediante un puerto accesible desde fuera del clúster (NodePort).

## 1. Desplegar los recursos

Aplica todos los manifiestos de la carpeta `stateless/` de forma simultánea:

```bash
kubectl apply -f stateless/
```

## 2. Verficar

```bash
kubectl get pods
kubectl exec -it deployment/color-app -- env | grep APP_COLOR   # debería mostrar azul
kubectl get svc color-svc
# Acceder vía NodePort (service color-svc)
```

## 3. Limpieza

```bash
kubectl delete -f stateless/
```
