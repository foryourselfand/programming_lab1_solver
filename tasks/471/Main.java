public class Main {
	public static void main(String[] args) {
		short[] b = {18, 16, 14, 12, 10, 8, 6, 4};
		
		float[] x = new float[18];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 22.0 - 12.0);
				
		double[][] k = new double[8][18];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) b[i]) {
					case 12:
						k[i][j] = Math.tan(Math.pow((1/4*Math.atan((x[j]-1)/22)), (Math.atan((x[j]-1)/22))));
						break;
					case 8:
					case 10:
					case 16:
					case 18:
						k[i][j] = Math.cbrt(Math.pow((Math.pow(Math.E, (x[j]))), 2));
						break;
					default:
						k[i][j] = Math.cbrt(Math.pow((Math.sin(Math.cbrt(x[j]))), (Math.log(Math.pow(Math.cos(x[j]), 2))/2)));
						break;
				}
				System.out.printf("%.5f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
