## Demonstração de API em Python com MySQL rodando em Kubernetes

### Requisitos

- Docker - https://docs.docker.com/get-started/get-docker/
- Kind   - https://kind.sigs.k8s.io/docs/user/quick-start/#installation

### Instruções

1. **Faça o fork do repositório e baixe os arquivos.**

2. **Inicie o cluster utilizando o Kind:**
   ```bash
   kind create cluster --config cluster-desafio-api/kind-cluster.yml --name desafio-rocketseat
   ```
   O cluster será iniciado com 1 nó de Control Plane e 1 nó de Worker.

3. **Mude o contexto do kubectl:**
   ```bash
   kubectl cluster-info --context kind-desafio-rocketseat
   ```

4. **Instale o Metric Server no cluster:**
   ```bash
   kubectl apply -f ./cluster-desafio-api/components.yml
   ```

5. **Crie o Storage Class:**
   ```bash
   kubectl apply -f ./cluster-desafio-api/storageclass.yml
   ```

6. **Crie o Persistent Volume para persistência do banco de dados MySQL:**
   ```bash
   kubectl apply -f ./cluster-desafio-api/pv.yml
   ```

7. **Crie os namespaces para aplicação e banco de dados:**
   ```bash
   kubectl create namespace desafio-api
   kubectl create namespace desafio-db
   ```

8. **Crie os componentes do banco de dados MySQL:**
   ```bash
   kubectl apply -f ./db/k8s/. -n desafio-db
   ```

9. **Crie os componentes da aplicação:**
   ```bash
   kubectl apply -f ./k8s/. -n desafio-api
   ```

### Acesso à aplicação

```
http://localhost:5000/status
```

### Testando chamadas e inserção de dados

- Importe o arquivo `Api Python Kubernetes.postman_collection.json` no Postman para testar os endpoints.
- Você também pode usar o cURL:

- Inserir dados
  ```bash
  curl -X POST http://localhost:5000/dados -H "Content-Type: application/json" -d '{"name": "João", "email": "joao@email.com"}'
  ```
- Consultar dados
  ```bash
  curl http://localhost:5000/consulta
  ```
- Consultar status da API
  ```bash
  curl http://localhost:5000/status
  ```

### Consultando logs da aplicação

```bash
kubectl logs <nome_do_pod> -n desafio-api
```

---

Feito com 💜





