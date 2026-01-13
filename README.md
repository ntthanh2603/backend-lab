# Backend Development Curriculum

Khi code thì tạo branch theo kiểu `name-topic/name` chú ý đùng để mất code khi conflict :)).

## 📚 Phần I: CƠ BẢN

### Module 1: Giới thiệu và CRUD cơ bản

**Mục tiêu**: Xây dựng nền tảng backend vững chắc

#### 1.1 Tổng quan Backend Development

- Vai trò của backend trong kiến trúc web
- Client-Server model và HTTP protocol
- REST API là gì và tại sao quan trọng
- Môi trường development setup (Node.js/Python/Java/Go)

#### 1.2 Database Fundamentals

- **SQL vs NoSQL**: Khi nào dùng gì?
- Thiết kế database schema
  - Primary keys, Foreign keys
  - Relationships: One-to-One, One-to-Many, Many-to-Many
  - Normalization và Denormalization
- **Database Indexing**
  - B-tree indexes, Hash indexes
  - Composite indexes
  - Query optimization
- **Transactions và ACID**
  - Atomicity, Consistency, Isolation, Durability
  - Transaction isolation levels
- **Database Migrations**
  - Version control cho database
  - Up/Down migrations
- **ORM/ODM** (Object-Relational/Document Mapping)
  - Prisma, TypeORM, Sequelize, Mongoose
  - N+1 query problem và cách giải quyết

#### 1.3 CRUD Operations

- Tạo ứng dụng CRUD hoàn chỉnh
- Best practices cho mỗi operation
- Soft delete vs Hard delete
- Pagination, Filtering, Sorting

---

### Module 2: Kiến trúc dự án và Authentication

**Mục tiêu**: Cấu trúc code professional và bảo mật

#### 2.1 Project Structure

- **Clean Architecture / Layered Architecture**
  - Controllers/Handlers
  - Services/Business Logic
  - Repositories/Data Access Layer
  - Models/Entities
- **Dependency Injection**
- Environment variables và configuration management
- Separation of Concerns

#### 2.2 Middleware

- Request lifecycle
- Custom middleware development
- Error handling middleware
- Logging middleware
- CORS middleware
- Rate limiting middleware

#### 2.3 Authentication & Authorization

- **Authentication Methods**
  - Session-based (Stateful)
  - Token-based (Stateless)
  - Cookie vs Token
- **JWT (JSON Web Tokens)**
  - Access tokens và Refresh tokens
  - Token rotation strategies
  - Token storage best practices
- **OAuth 2.0 & OpenID Connect**
  - Authorization Code Flow
  - Implicit Flow
  - Client Credentials Flow
- **Single Sign-On (SSO)**
- **Multi-Factor Authentication (MFA)**
- **Role-Based Access Control (RBAC)**
- **Permission-Based Access Control**

---

### Module 3: API Design và Error Handling

**Mục tiêu**: Xây dựng API chuẩn và dễ maintain

#### 3.1 RESTful API Best Practices

- HTTP methods đúng cách (GET, POST, PUT, PATCH, DELETE)
- Status codes chuẩn (2xx, 4xx, 5xx)
- Resource naming conventions
- **API Versioning**
  - URI versioning (/v1/, /v2/)
  - Header versioning
  - Query parameter versioning
- **HATEOAS** (Hypermedia as the Engine of Application State)
- **API Documentation**
  - Swagger/OpenAPI specification
  - Postman collections
  - API changelog

#### 3.2 Request Validation

- **DTO (Data Transfer Objects)**
- Input validation libraries (Joi, Yup, Zod, class-validator)
- Sanitization để tránh injection attacks
- Custom validation rules

#### 3.3 Error Handling

- Centralized error handling
- Custom error classes
- Error response standardization
- Stack trace management (dev vs production)
- Graceful error recovery

#### 3.4 Logging & Monitoring

- Structured logging (Winston, Pino, Bunyan)
- Log levels (debug, info, warn, error)
- Log aggregation (ELK stack, Datadog)
- Request/Response logging
- Performance monitoring

---

### Module 4: File Upload và Storage

**Mục tiêu**: Xử lý file upload an toàn và hiệu quả

#### 4.1 File Upload Basics

- Multipart form data
- File size limits và validation
- File type validation (MIME types)
- Progress tracking

#### 4.2 Storage Solutions

- **Local storage**
  - File system organization
  - Serving static files
- **Cloud storage**
  - AWS S3
  - Google Cloud Storage
  - Azure Blob Storage
- **CDN integration**

#### 4.3 Image Processing

- Resize và optimization
- Format conversion
- Thumbnail generation
- Libraries: Sharp, Jimp

#### 4.4 Security

- File upload vulnerabilities
- Virus scanning
- Access control cho files
- Signed URLs

---

### Module 5: Real-time Communication

**Mục tiêu**: Xây dựng ứng dụng real-time

#### 5.1 WebSocket

- WebSocket protocol overview
- Socket.io implementation
- Room và namespace management
- Authentication trong WebSocket
- Scaling WebSocket (Redis adapter)

#### 5.2 Server-Sent Events (SSE)

- SSE vs WebSocket
- Use cases cho SSE
- Implementation

#### 5.3 Long Polling

- Khi nào sử dụng
- Trade-offs

---

### Module 6: Testing

**Mục tiêu**: Đảm bảo chất lượng code

#### 6.1 Testing Fundamentals

- Testing pyramid
- TDD (Test-Driven Development) approach
- AAA pattern (Arrange, Act, Assert)

#### 6.2 Unit Testing

- Testing frameworks (Jest, Mocha, Vitest)
- Mocking và stubbing
- Testing services và repositories
- Code coverage targets

#### 6.3 Integration Testing

- Database integration tests
- API endpoint testing
- Test databases và fixtures

#### 6.4 End-to-End Testing

- E2E testing tools (Supertest, Playwright)
- Testing complete user flows
- Testing với external services

#### 6.5 Best Practices

- Test naming conventions
- Test organization
- Continuous Integration (CI) setup
- Test performance optimization

---

## 🚀 Phần II: NÂNG CAO

### Module 7: Performance Optimization

**Mục tiêu**: Tối ưu hiệu suất hệ thống

#### 7.1 Caching Strategies

- **Cache Patterns**
  - Cache-Aside (Lazy Loading)
  - Write-Through
  - Write-Behind
  - Refresh-Ahead
- **Redis Deep Dive**
  - Data structures (String, Hash, List, Set, Sorted Set)
  - Pub/Sub messaging
  - Redis Streams
  - Transactions
  - Lua scripting
  - Redis Cluster và Sentinel
- **Cache Invalidation**
  - Time-based (TTL)
  - Event-based
  - Tag-based
- **HTTP Caching**
  - ETag
  - Cache-Control headers
  - Last-Modified

#### 7.2 Database Optimization

- Query optimization techniques
- Connection pooling
- Read replicas
- Database sharding
- Partitioning strategies

#### 7.3 Application Performance

- Profiling và bottleneck identification
- Memory leaks detection
- Load testing (Artillery, k6)
- APM tools (New Relic, Datadog)

---

### Module 8: Asynchronous Processing

**Mục tiêu**: Xử lý tác vụ nền hiệu quả

#### 8.1 Message Queue Systems

- **Why Message Queues?**
  - Decoupling services
  - Load leveling
  - Reliability và fault tolerance

#### 8.2 BullMQ (Redis-based)

- Job creation và processing
- Job priorities
- Job retries và backoff strategies
- Concurrency control
- Job events và monitoring
- Queue metrics

#### 8.3 Apache Kafka

- **Kafka Architecture**
  - Topics, Partitions, Brokers
  - Producers và Consumers
  - Consumer Groups
- **Event Streaming**
- **Kafka Connect**
- **Stream processing với Kafka Streams**
- **Use cases**: Event sourcing, Log aggregation, Real-time analytics

#### 8.4 RabbitMQ

- Exchange types (Direct, Topic, Fanout, Headers)
- Routing patterns
- Message acknowledgment

---

### Module 9: Job Scheduling

**Mục tiêu**: Tự động hóa tác vụ định kỳ

#### 9.1 Scheduling Concepts

- Cron expressions
- Distributed scheduling challenges
- Idempotency

#### 9.2 Implementation

- **node-cron / node-schedule**
- **Agenda / Bull scheduler**
- **Kubernetes CronJobs**

#### 9.3 Best Practices

- Error handling và retries
- Job monitoring và alerting
- Preventing overlapping executions
- Job history và audit logs

---

### Module 10: Security Deep Dive

**Mục tiêu**: Bảo mật toàn diện

#### 10.1 OWASP Top 10 (2021)

1. **Broken Access Control**
   - Horizontal và vertical privilege escalation
   - IDOR (Insecure Direct Object References)
2. **Cryptographic Failures**
   - Encryption at rest và in transit
   - Password hashing (bcrypt, argon2)
3. **Injection**
   - SQL Injection
   - NoSQL Injection
   - Command Injection
   - Prevention: Parameterized queries, ORM
4. **Insecure Design**
   - Threat modeling
   - Secure by design principles
5. **Security Misconfiguration**
   - Default credentials
   - Unnecessary features enabled
6. **Vulnerable and Outdated Components**
   - Dependency scanning
   - Regular updates
7. **Identification and Authentication Failures**
   - Session management
   - Credential stuffing protection
8. **Software and Data Integrity Failures**
   - Unsigned updates
   - CI/CD pipeline security
9. **Security Logging and Monitoring Failures**
   - Audit logging
   - Alerting systems
10. **Server-Side Request Forgery (SSRF)**
    - URL validation
    - Network segmentation

#### 10.2 Additional Security Topics

- **HTTPS/TLS**
- **Content Security Policy (CSP)**
- **CSRF Protection**
- **Rate Limiting và DDoS protection**
- **Input sanitization**
- **Security headers** (Helmet.js)
- **Secrets management** (Vault, AWS Secrets Manager)
- **Penetration testing basics**

---

### Module 11: Design Patterns

**Mục tiêu**: Code maintainable và scalable

#### 11.1 Creational Patterns

- **Singleton**: Database connections, Configuration
- **Factory**: Object creation flexibility
- **Builder**: Complex object construction
- **Dependency Injection**: Loose coupling

#### 11.2 Structural Patterns

- **Repository Pattern**: Data access abstraction
- **Adapter Pattern**: Interface compatibility
- **Decorator Pattern**: Extending functionality
- **Proxy Pattern**: Access control

#### 11.3 Behavioral Patterns

- **Strategy Pattern**: Algorithm selection
- **Observer Pattern**: Event handling
- **Chain of Responsibility**: Middleware chains
- **Command Pattern**: Request encapsulation

#### 11.4 Architectural Patterns

- **Service Layer Pattern**
- **CQRS** (Command Query Responsibility Segregation)
- **Event Sourcing**
- **Saga Pattern** (Distributed transactions)

---

### Module 12: Microservices Architecture

**Mục tiêu**: Thiết kế hệ thống phân tán

#### 12.1 Microservices Fundamentals

- Monolith vs Microservices
- When to use microservices
- Service decomposition strategies
- **API Gateway**
  - Kong, AWS API Gateway
  - Rate limiting, Authentication
- **Service Discovery**
  - Consul, Eureka
- **Service Mesh**
  - Istio, Linkerd

#### 12.2 Inter-Service Communication

- **Synchronous**: REST, gRPC
- **Asynchronous**: Message queues, Event bus
- **Service-to-service authentication**
- **Circuit Breaker pattern** (Resilience4j, Hystrix)
- **Retry policies và timeouts**

#### 12.3 Data Management

- Database per service
- Distributed transactions
- **Saga pattern**
- **Event-driven architecture**
- Data consistency challenges (CAP theorem)

#### 12.4 Observability

- **Distributed Tracing** (Jaeger, Zipkin)
- **Centralized Logging** (ELK Stack, Loki)
- **Metrics** (Prometheus, Grafana)
- **Health checks**

---

### Module 13: Domain-Driven Design (DDD)

**Mục tiêu**: Thiết kế phần mềm phức tạp

#### 13.1 DDD Strategic Design

- **Ubiquitous Language**
- **Bounded Contexts**
- **Context Mapping**
  - Shared Kernel
  - Customer-Supplier
  - Conformist
  - Anti-Corruption Layer
- **Subdomains**: Core, Supporting, Generic

#### 13.2 DDD Tactical Design

- **Entities**: Identity và lifecycle
- **Value Objects**: Immutability
- **Aggregates**: Consistency boundaries
- **Repositories**: Persistence abstraction
- **Domain Services**: Complex business logic
- **Domain Events**: Communication giữa aggregates
- **Factories**: Object creation

#### 13.3 Application Architecture

- **Hexagonal Architecture** (Ports & Adapters)
- **Clean Architecture**
- **Onion Architecture**
- Separation of domain logic từ infrastructure

---

## 🎯 Phần III: CÁC CHỦ ĐỀ BỔ SUNG QUAN TRỌNG

### Module 14: API Advanced Topics

#### 14.1 GraphQL

- GraphQL vs REST
- Schema definition
- Resolvers
- Queries, Mutations, Subscriptions
- N+1 problem và DataLoader
- GraphQL best practices

#### 14.2 gRPC

- Protocol Buffers
- Streaming (Server, Client, Bidirectional)
- Use cases cho gRPC
- REST vs gRPC comparison

#### 14.3 API Rate Limiting

- Fixed window, Sliding window
- Token bucket algorithm
- Implementation strategies

#### 14.4 API Pagination

- Offset-based pagination
- Cursor-based pagination
- Keyset pagination
- Performance considerations

---

### Module 15: DevOps Essentials

#### 15.1 Containerization

- **Docker**
  - Dockerfile best practices
  - Multi-stage builds
  - Docker Compose
- **Container orchestration basics**
  - Kubernetes overview
  - Pods, Services, Deployments

#### 15.2 CI/CD

- **Continuous Integration**
  - GitHub Actions, GitLab CI, Jenkins
  - Automated testing
  - Code quality checks (ESLint, SonarQube)
- **Continuous Deployment**
  - Blue-Green deployment
  - Canary releases
  - Rolling updates

#### 15.3 Infrastructure as Code

- **Configuration management**
- **Terraform basics**
- **Ansible basics**

#### 15.4 Cloud Platforms (AWS/GCP/Azure)

- Compute services (EC2, Cloud Run, App Service)
- Managed databases (RDS, Cloud SQL)
- Object storage (S3, Cloud Storage)
- Serverless (Lambda, Cloud Functions)
