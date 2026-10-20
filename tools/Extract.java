import jadx.api.*;
import java.io.*;
import java.nio.file.*;
import java.util.*;
class Extract {
 public static void main(String[] a) throws Exception {
  JadxArgs opts=new JadxArgs(); opts.setInputFiles(List.of(new File(a[0]))); opts.setSkipResources(true); opts.setThreadsCount(2);
  try(JadxDecompiler d=new JadxDecompiler(opts)) {d.load();
   List<String> names=new ArrayList<>();
   for(JavaClass c:d.getClasses()) {String n=c.getFullName(); names.add(n); if(n.toLowerCase().contains(a[2].toLowerCase())) {try {Files.writeString(Path.of(a[1],n+".java"),c.getCode());System.out.println(n);}catch(Exception e){System.err.println(n+":"+e);}}}
   Files.write(Path.of(a[1],"class-index.txt"),names);
  }
 }
}
