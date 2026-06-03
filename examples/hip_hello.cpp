#include <hip/hip_runtime.h>
#include <iostream>

__global__ void hello_kernel() {
    printf("[hip_hello] block(%d,%d,%d) thread(%d,%d,%d)\n",
           blockIdx.x, blockIdx.y, blockIdx.z,
           threadIdx.x, threadIdx.y, threadIdx.z);
}

int main() {
    std::cout << "[hip_hello] launching kernel\n";
    hello_kernel<<<1, 4>>>();
    hipDeviceSynchronize();
    std::cout << "[hip_hello] done\n";
    return 0;
}
