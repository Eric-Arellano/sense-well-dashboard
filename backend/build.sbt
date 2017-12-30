name := "sense-well-backend"

version := "0.1"

scalaVersion := "2.12.3"

libraryDependencies += "org.scalactic" %% "scalactic" % "3.0.1"
libraryDependencies += "org.scalatest" %% "scalatest" % "3.0.1" % "test"
libraryDependencies += "com.typesafe.akka" %% "akka-http"   % "10.1.0-RC1"
libraryDependencies += "com.typesafe.akka" %% "akka-stream" % "2.5.8"


resolvers += "Artima Maven Repository" at "http://repo.artima.com/releases"
