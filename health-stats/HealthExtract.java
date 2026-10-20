import jadx.api.*;
import java.io.*;
import java.nio.file.*;
import java.util.*;
class HealthExtract {
 public static void main(String[] a) throws Exception {
  JadxArgs opts=new JadxArgs(); opts.setInputFiles(List.of(new File(a[0]))); opts.setSkipResources(true); opts.setThreadsCount(1);
  Set<String> exact=new HashSet<>(Arrays.asList(a[2].split(",")));
  try(JadxDecompiler d=new JadxDecompiler(opts)) { d.load();
   for(JavaClass c:d.getClasses()) {String n=c.getClassNode().getClassInfo().getRawName(); String low=n.toLowerCase();
    if(exact.contains(n) || exact.stream().anyMatch(x -> x.endsWith(".") && n.startsWith(x)) || (n.startsWith("com.garmin.") && low.matches(".*(dailysummary|usersummary|sleepdata|sleepdto|hrvsummary|hrvdata|bodybattery|stressdata|hydrationdata|weightdata|bloodpressure|respirationdata|trainingreadiness|fitnessage|heartratedata|pulseoxdata).*"))) {
     try {Files.writeString(Path.of(a[1],n+".java"),c.getCode());System.out.println(n);}catch(Exception e){System.err.println(n+":"+e);}
    }
   }
  }
 }
}
