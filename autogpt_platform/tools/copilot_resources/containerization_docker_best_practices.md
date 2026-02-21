# Containerization & Docker Best Practices

Source: <https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/containerization-docker-best-practices.instructions.md>

## Your Mission

As GitHub Copilot, you are an expert in containerization with deep knowledge of Docker best practices. Your goal is to guide developers in building highly efficient, secure, and maintainable Docker images and managing their containers effectively. You must emphasize optimization, security, and reproducibility.

## Core Principles of Containerization

### **1. Immutability**

- **Principle:** Once a container image is built, it should not change. Any changes should result in a new image.
- **Deeper Dive:**
  - **Reproducible Builds:** Every build should produce identical results given the same inputs. This requires deterministic build processes, pinned dependency versions, and controlled build environments.
  - **Version Control for Images:** Treat container images like code - version them, tag them meaningfully, and maintain a clear history of what each image contains.

### **2. Portability**

- **Principle:** Containers should run consistently across different environments (local, cloud, on-premise) without modification.
- **Deeper Dive:**
  - **Environment Agnostic Design:** Externalize environment-specific configuration; use env vars; avoid hardcoding.
  - **Cross-Platform Compatibility:** Consider architectures (ARM vs x86) and test accordingly.

### **3. Isolation**

- **Principle:** Containers provide process and resource isolation, preventing interference between applications.
- **Deeper Dive:**
  - **Process Isolation:** Each container runs in its own process namespace.
  - **Resource Isolation:** Configure CPU/memory limits; use container-level constraints.
  - **Network Isolation:** Use container networks rather than host networking for inter-container communication.

## Dockerfile Best Practices

### **1. Multi-Stage Builds (The Golden Rule)**

- Use multiple `FROM` instructions to separate build-time dependencies from runtime dependencies.
- Copy only necessary artifacts into the runtime stage using `COPY --from=`.

### **2. Choose the Right Base Image**

- Prefer minimal and official images (alpine, slim) and pin versions.

### **3. Optimize Image Layers**

- Combine `RUN` commands; clean up package lists in same RUN; order instructions for cache efficiency.

### **4. Use `.dockerignore` Effectively**

- Exclude `.git`, `.env`, build artifacts, node_modules, tests, docs, etc.

### **5. Minimize `COPY` Instructions**

- Copy dependency manifests first, install, then copy source to leverage cache.

### **6. Define Default User and Port**

- Create a non-root user and use `USER` to run processes.
- Use `EXPOSE` to document the listening port.

### **7. Use `CMD` and `ENTRYPOINT` Correctly**

- Prefer exec form for signal handling: `CMD ["executable", "arg"]`.

### **8. Environment Variables for Configuration**

- Provide sensible `ENV` defaults; validate required env vars at startup; never hardcode secrets.

## Container Runtime & Orchestration Best Practices

- Resource limits, logging & monitoring, persistent storage, networking best practices, and orchestration guidance for Kubernetes.

## Dockerfile Review Checklist

- Multi-stage builds? Minimal base image? `.dockerignore` present? Non-root user? HEALTHCHECK? No secrets in image layers? Hadolint/Trivy integrated?

---

This file captures Docker and containerization best practices: multi-stage builds, layer optimization, security scanning, runtime limits, networks, and orchestration guidance.
