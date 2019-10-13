public class Main {
	public static void main(String[] args) {
		long[] d = {4, 6, 8, 10, 12, 14, 16, 18, 20, 22};
		
		float[] x = new float[20];
		for (int i = 0; i < x.length; i++)
			x[i] = (float) (Math.random() * 11.0 - 7.0);
				
		double[][] k = new double[10][20];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) d[i]) {
					case 8:
						k[i][j] = Math.pow(Math.E, (Math.asin(Math.pow(((x[j]-1.5)/11), 2))));
						break;
					case 4:
					case 6:
					case 10:
					case 12:
					case 22:
						k[i][j] = 1/3/(2*Math.tan(x[j])-3);
						break;
					default:
						k[i][j] = Math.pow(((Math.sin(Math.log(Math.pow((Math.abs(x[j])/Math.PI), (x[j]))))-Math.PI)/0.5), 2);
						break;
				}
				System.out.printf("%.2f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
