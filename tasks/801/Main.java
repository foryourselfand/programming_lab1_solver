public class Main {
	public static void main(String[] args) {
		short[] a = {19, 17, 15, 13, 11, 9, 7, 5, 3, 1};
		
		float[] x = new float[20];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 14.0 - 11.0);
				
		double[][] p = new double[10][20];
		for (int i = 0; i < p.length; i++) {
			for (int j = 0; j < p[i].length; j++) {
				switch ((int) a[i]) {
					case 19:
						p[i][j] = Math.log(Math.pow(Math.sin(Math.pow(Math.E, (Math.sin(x[j])))), 2));
						break;
					case 1:
					case 7:
					case 9:
					case 13:
					case 15:
						p[i][j] = Math.pow((1/2/Math.pow(((3/4-x[j])/3/4), (x[j]))/(1-Math.asin((x[j]-4)/14))), 3);
						break;
					default:
						p[i][j] = Math.pow(Math.E, (Math.pow((Math.pow((2*Math.cbrt(x[j])), 3)), ((Math.PI-Math.cos(Math.pow(((0.25-x[j])/2/3), 2)))/Math.tan(Math.tan(x[j]))))));
						break;
				}
				System.out.printf("%.3f ", p[i][j]);
			}
			System.out.println();
		}
	}
}
