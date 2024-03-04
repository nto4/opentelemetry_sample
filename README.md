# STRUCTURE

#### metrics 
APP --> OTEL-COLLECTOR --> prometheus

#### traces 
APP --> OTEL-COLLECTOR -->  zipkin

#### logs
APP --> OTEL-COLLECTOR -->  elasticsearch 

### Demo app  build
sizin iletitğiniz projeyi  çekip
trace ve metrikleri çekmek için Automatic Instrumentation jarını  demo porjenin runtimına ekledım  ek olarak daha detaytlı metrik çekmek için  projede ekli olan actuator un prometheus endpointini açtım


src/main/resources/application.yml

management:
  endpoints:
    web:
      exposure:
        include: health,info,prometheus

pom.xml
                <dependency>
                        <groupId>io.micrometer</groupId>
                        <artifactId>micrometer-registry-prometheus</artifactId>
                        <scope>runtime</scope>
                </dependency>



https://opentelemetry.io/docs/languages/java/automatic/


docker build -t java-demoapp


# durum
bu yapı ile uygulamanın tracelerini çekebildim uygulamanın koştuğu podun metriklerini çekebildim
log çekmede sorun yaşıyorum ama başka proje denediğimde logda çekebildim demo projesinin logger ayarlarında değişiklik yapmak gerekiyor ama bunu yapamadım.

#### traces
![all traces for demo app](image.png)

![only error tagged traces](image-1.png)

![for one  error trace all spans](image-2.png)

![for one  error trace all spans table](image-3.png)

#### metrics
![otel collector metrics](image-4.png)

![demo app metrics received from otel collector](image-5.png)

![demo app actuator metrics](image-8.png)

![prometheus showcase](image-6.png)

![jvm memory useage in demo app](image-7.png)

#### logs
automatic insturumented ajanı ile logu console  export edebıldım ama  otlp den elasticsearche yonelendırmede  sorun yaşadım bunu henüz çözemedim.


