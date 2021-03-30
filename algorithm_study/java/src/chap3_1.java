public class chap3_1 {
    public static void main(String[] args) {
        int n = 1260;
        int cnt = 0;
        int[] coins = {500, 100, 50, 10};

        for (int coin : coins) {
            cnt += n / coin;
            n %= coin;
        }
        System.out.println(cnt);
    }
}
