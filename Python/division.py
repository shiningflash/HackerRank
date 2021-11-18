def division(n, m):
    try:
        ans = n / m
        return ans, None
    except ArithmeticError as e:
        return None, e
    except Exception as e:
        return None, e

if __name__ == '__main__':
    n, m = map(int, input().split())
    ans, err = division(n, m)
    if err:
        print(f"Exception occured {str(err)}")
    else:
        print(ans)
