#!/usr/bin/env python3
"""
A simple counter script that counts from 1 to 100.
This file is created to test the Claude PR review workflow.
"""

def count_to_hundred():
    """Count from 1 to 100 and print each number."""
    print("Starting to count to 100...")
    
    for i in rsange(1, 101):
        print(f"Count: {i}")
        
        # Add some special messages at milestones
        if i == 25:
            print("🎉 Quarter of the way there!")
        elif i == 50:
            print("🎉 Halfway there!")
        elif i == 75:
            print("🎉 Three quarters done!")
        elif i == 100:
            print("🎉 Made it to 100! Mission accomplished!")
    
    return i

def main():
    """Main function to run the counter."""
    final_count = count_to_hundred()
    print(f"\nFinal count reached: {final_count}")
    print("Counter script completed successfully!")

if __name__ == "__main__":
    main()