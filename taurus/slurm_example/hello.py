import time

if __name__ == "__main__":
    print("This message must be appear in hello_world.out")

    # We pause the execution for 10 seconds to check the sbatch with squeue --me
    time.sleep(10)

    with open("output_hello_world.txt", "w") as ftxt:
        ftxt.write("HELLO WORLD\n")
