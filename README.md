# Programming Lab1 Solver

## Task
Write a mathematical expression processing program using Java programming language (expressions are different for different task variants). Program should satisfy these requirements:

1. It should be packaged into executable jar archive.
2. Expression should be processed in coordination with mathematical equation rules (operations order etc.).
3. Program must use math functions from Java standard library (java.lang.math package).
4. Program should use standard output to display expression processing result.

Program demonstration should be performed using helios server.

## WARNING
It's not ready: ```1/2``` instead ```1.0 / 2.0``` or ```(double) (1 / 2)```

Also: if you variant not in remembered variants, update ```info/config.txt```
##Example

### Input
```python solver.py 698```

### Output
tasks/698/Main.java:

```java
public class Main {
	public static void main(String[] args) {
		short[] d = {18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5};
		
		double[] x = new double[20];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 16.0 - 12.0;
				
		double[][] f = new double[14][20];
		for (int i = 0; i < f.length; i++) {
			for (int j = 0; j < f[i].length; j++) {
				switch ((int) d[i]) {
					case 7:
						f[i][j] = Math.asin(Math.pow(Math.E, (Math.cbrt(-Math.pow(Math.sin(x[j]), 2)))));
						break;
					case 5:
					case 6:
					case 8:
					case 9:
					case 15:
					case 16:
					case 17:
						f[i][j] = Math.sin(Math.pow((3*(Math.cos(x[j])-1)), (Math.pow((3*x[j]), 3))));
						break;
					default:
						f[i][j] = Math.pow(Math.E, (Math.pow(Math.E, (4*(1/2+x[j])))))+1/2;
						break;
				}
				System.out.printf("%.3f ", f[i][j]);
			}
			System.out.println();
		}
	}
}
```