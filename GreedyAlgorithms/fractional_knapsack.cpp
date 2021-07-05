#include <iostream>
#include <vector>

#define ll long long

using std::vector;

void merge(vector < ll > & weights, vector < ll > & values, int lb, int mid, int ub) {
    int i, j, k, size;
    i = lb;
    j = mid + 1;
    k = 0;
    size = ub - lb + 1;

    double ratio_1, ratio_2;
    vector < ll > temp_weights(size);
    vector < ll > temp_values(size);

    while (i <= mid && j <= ub) {
        ratio_1 = (double) values[i] / weights[i];
        ratio_2 = (double) values[j] / weights[j];
        if (ratio_2 > ratio_1) {
            temp_weights[k] = weights[j];
            temp_values[k] = values[j];
            j++;
        } else {
            temp_weights[k] = weights[i];
            temp_values[k] = values[i];
            i++;
        }
        k++;
    }

    while (i <= mid) {
        temp_weights[k] = weights[i];
        temp_values[k] = values[i];
        i++;
        k++;
    }

    while (j <= ub) {
        temp_weights[k] = weights[j];
        temp_values[k] = values[j];
        j++;
        k++;
    }

    for (i = lb, k = 0; i <= ub; i++, k++) {
        weights[i] = temp_weights[k];
        values[i] = temp_values[k];
    }
}

void mergesort(vector < ll > & weights, vector < ll > & values, int lb, int ub) {
    if (lb < ub) {
        int mid = lb + (ub - lb) / 2;
        mergesort(weights, values, lb, mid);
        mergesort(weights, values, mid + 1, ub);
        merge(weights, values, lb, mid, ub);
    }
    return;
}

double get_optimal_value(int capacity, vector < ll > weights, vector < ll > values) {
    double value = 0.0;
    int curr_weight, i = 0;
    
	while (capacity && i < weights.size()) {
        curr_weight = capacity - weights[i];
		if (curr_weight >= 0) {
            capacity = curr_weight;
            value += (values[i]);
            // std::cout<<capacity<<" "<<value<<"\t";
            i++;
        } else {
			double ratio = (double) values[i] / weights[i];
            value += (double) capacity * ratio;
            // std::cout<<capacity<<" "<<value<<" "<<ratio<<"\t";
            capacity = 0;
        }
    }
        return value;
}

int main() {
    int n;
    int capacity;
    std::cin >> n >> capacity;

    vector < ll > values(n);
    vector < ll > weights(n);

    for (int i = 0; i < n; i++) {
        std::cin >> values[i] >> weights[i];
    }

    mergesort(weights, values, 0, n - 1);
    // std::cout<<std::endl;
    // for (int i=0; i<n; i++) {
    //     std::cout<<values[i]<<" "<<weights[i]<<"\t";
    // }

    double optimal_value = get_optimal_value(capacity, weights, values);

    std::cout.precision(10);
    std::cout << optimal_value << std::endl;

    return 0;
}