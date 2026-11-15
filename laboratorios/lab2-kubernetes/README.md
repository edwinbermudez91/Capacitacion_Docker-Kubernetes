# ☸️ Lab 2: Despliegues en Kubernetes (Stateless vs Stateful)

En este bloque aprenderás la diferencia práctica entre desplegar aplicaciones **sin estado (Stateless)** y aplicaciones **con estado (Stateful)** en Kubernetes.

```mermaid
flowchart LR
    subgraph S1["Lab 2A: Stateless"]
        D["Deployment: color-app"] -->|"Réplicas intercambiables"| SVC1["Service: color-svc<br/>(NodePort)"]
        CM["ConfigMap: app-config"] -.->|"Variables"| D
    end

    subgraph S2["Lab 2B: Stateful"]
        STS["StatefulSet: mysql-db<br/>(mysql-db-0, mysql-db-1)"] -->|"DNS estable"| HL["Headless Service<br/>(mysql-headless)"]
        SEC["Secret: db-credentials"] -.->|"Credenciales"| STS
        ADM["Adminer (Deployment)"] -->|"Conecta vía DNS"| HL
    end

    style S1 fill:#eff6ff,stroke:#2563eb,color:#1e3a8a
    style S2 fill:#f5f3ff,stroke:#7c3aed,color:#4c1d95
```

## 📂 Ejercicios Disponibles

| Orden | Ejercicio | Conceptos Clave | Guía |
| :---: | :--- | :--- | :---: |
| **2A** | **Aplicación Web Stateless** | `Deployment`, `ConfigMap`, `Service (NodePort)` | [🌐 Ir al Ejercicio Stateless](./ejercicio-stateless.md) |
| **2B** | **Base de Datos Stateful + Adminer** | `StatefulSet`, `Secret`, `Headless Service`, DNS interno | [🗄️ Ir al Ejercicio Stateful](./ejercicio-stateful.md) |

---

<div align="center">

[⬅️ Lab 1B: Secure Translator](../lab1-docker/translate/README.md) · [🏠 Índice Principal](../../README.md) · [Lab 2A: Stateless ➡️](./ejercicio-stateless.md)

</div>
