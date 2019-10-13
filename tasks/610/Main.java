public class Main {
	public static void main(String[] args) {
		long[] c = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22};
		
		float[] x = new float[12];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 9.0 - 5.0);
				
		double[][] g = new double[11][12];
		for (int i = 0; i < g.length; i++) {
			for (int j = 0; j < g[i].length; j++) {
				switch ((int) c[i]) {
					case 4:
						g[i][j] = Math.pow((Math.cos(Math.pow((2*x[j]), 3))/(1/2-Math.sin(Math.asin((x[j]-0.5)/9)))), 3);
						break;
					case 6:
					case 10:
					case 14:
					case 16:
					case 20:
						g[i][j] = Math.pow(((Math.cbrt(x[j])-4)/2/3), (Math.pow((2*x[j]), 3)))*(Math.log(Math.pow(Math.tan, 2)(x[j]))+3/4);
						break;
					default:
						g[i][j] = Math.pow((Math.asin(Math.pow(1/Math.E, (Math.pow((Math.pow((Math.abs(x[j])/2), 2+1)), 2))))), (Math.pow((Math.tan(Math.cos(x[j]))), (Math.tan(Math.sin(x[j]))-2))));
						break;
				}
				System.out.printf("%.3f ", g[i][j]);
			}
			System.out.println();
		}
	}
}
