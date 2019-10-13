public class Main {
	public static void main(String[] args) {
		short[] d = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23};
		
		double[] x = new double[16];
		for (int i = 0; i < x.length; i++)
			x[i] = Math.random() * 6.0 - 2.0;
				
		double[][] k = new double[11][16];
		for (int i = 0; i < k.length; i++) {
			for (int j = 0; j < k[i].length; j++) {
				switch ((int) d[i]) {
					case 21:
						k[i][j] = Math.cos(Math.pow(Math.E, (Math.cbrt(x[j]))));
						break;
					case 5:
					case 9:
					case 11:
					case 19:
					case 23:
						k[i][j] = Math.sin(Math.pow((x[j]/3), (3/4*Math.atan((x[j]+1)/6))));
						break;
					default:
						k[i][j] = Math.pow((Math.tan(Math.pow(Math.E, (Math.pow((3/4*(2+x[j])), 2))))), ((Math.tan(x[j])/2/3/(Math.sin(x[j])-1)+1)/1/4));
						break;
				}
				System.out.printf("%.2f ", k[i][j]);
			}
			System.out.println();
		}
	}
}
