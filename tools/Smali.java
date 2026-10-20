import jadx.api.*;
import java.io.*;
import java.nio.file.*;
import java.util.*;
class Smali {
 public static void main(String[] a) throws Exception {
  JadxArgs opts=new JadxArgs(); opts.setInputFiles(List.of(new File(a[0]))); opts.setSkipResources(true); opts.setThreadsCount(2);
  try(JadxDecompiler d=new JadxDecompiler(opts)) {d.load();
   List<String> names=new ArrayList<>();
   for(JavaClass c:d.getClasses()) {String n=c.getClassNode().getClassInfo().getRawName(); names.add(n); if(java.util.Arrays.stream(a[2].split(",")).anyMatch(n::startsWith) || c.getClassNode().getMethods().stream().anyMatch(m -> String.valueOf(m.getAttributesString()).contains("workout-service"))) {try {Files.writeString(Path.of(a[1],n+".smali"),c.getSmali());System.out.println(n);}catch(Exception e){System.err.println(n+":"+e);}}}
   Files.write(Path.of(a[1],"targeted-class-index.txt"),names);
  }
 }
}
