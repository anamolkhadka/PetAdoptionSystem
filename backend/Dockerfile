# syntax=docker/dockerfile:1

# Stage 1: Build the application with Gradle
FROM eclipse-temurin:17-jdk-jammy as build

WORKDIR /app

# Copy the Gradle wrapper and configuration files
COPY examples/gradlew examples/settings.gradle examples/build.gradle ./

# Copy the Gradle directory if it exists
COPY examples/gradle ./gradle

# Download Gradle dependencies to leverage Docker caching
RUN ./gradlew dependencies --no-daemon

# Copy the source code
COPY examples/src ./src

# Build the application using Gradle
RUN ./gradlew installDist --no-daemon

################################################################################

# Stage 2: Create a minimal image to run the application
FROM eclipse-temurin:17-jre-jammy as final

# Copy the built application from the previous stage
COPY --from=build /app/build/install/examples /app

# Expose the gRPC server port
EXPOSE 50052

# Start the gRPC server
CMD ["/app/bin/pet-adoption-server"]