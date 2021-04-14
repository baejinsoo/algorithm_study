import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Kakao1 {

    public static int solution(int[] gift_cards, int[] wants) {
        int answer = 0;
        int[] arr = new int[wants.length];
        for (int i = 0; i < wants.length; i++) {
            arr[gift_cards[i] - 1] += 1;
        }
        for (int i = 0; i < wants.length; i++) {
            if (wants[i] == gift_cards[i]) {
                arr[wants[i] - 1] = 0;
                answer -= 1;
            }
        }
        for (int j = 0; j < wants.length; j++) {
            if (arr[wants[j] - 1] == 0) {
                answer += 1;
            }
            else if (arr[wants[j]-1] > 0) {
                arr[wants[j]-1] -= 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] gift_cards = {5,4,5,4,5};
        int[] wants = {1,2,3,5,4};
        int res = solution(gift_cards, wants);
        System.out.println(res);
    }
}
