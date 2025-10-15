import math
from scipy.stats import norm


class Option:
    def __init__(self, s: float, k: float, r: float, ttm: float, sigma: float):
        self.S = s
        self.K = k
        self.r = r
        self.T = ttm
        self.sigma = sigma

    def d1(self):
        return (math.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / self.sigma * math.sqrt(self.T)

    def d2(self):
        return self.d1() - self.sigma * math.sqrt(self.T)

    def vega(self):
        return self.S * norm.pdf(self.d1()) * math.sqrt(self.T)


class Call(Option):
    def price(self):
        d1, d2 = self.d1(), self.d2()
        return self.S * norm.cdf(d1) - self.K * math.exp(-self.r * self.T) * norm.cdf(d2)

    def delta(self):
        return norm.cdf(self.d1())

    def rho(self):
        return self.T * self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2())

    def theta(self):
        d1, d2 = self.d1(), self.d2()
        return (-(self.S * norm.pdf(d1) * self.sigma) / (2 * math.sqrt(self.T))
                -self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(d2))

    def theta_per_day(self):
        return self.theta() / 365.0


class Put(Option):
    def price(self):
        d1, d2 = self.d1(), self.d2()
        return self.K * math.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)

    def delta(self):
        return norm.cdf(self.d1()) - 1.0

    def rho(self):
        return -self.T * self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2())

    def rho_per_1pct(self):
        return 0.01 * self.rho()

    def theta(self):
        d1, d2 = self.d1(), self.d2()
        return (-(self.S * norm.pdf(d1) * self.sigma) / (2 * math.sqrt(self.T)) + self.r * self.K *
                math.exp(-self.r * self.T) * norm.cdf(-d2))

    def theta_per_day(self):
        return self.theta() / 365.0


if __name__ == "__main__":
    call = Call(s=200, k=250, r=0.05, ttm=1.0, sigma=0.15)
    put  = Put (s=200, k=250, r=0.05, ttm=1.0, sigma=0.15)

    print(f"Call price: {call.price():.2f}")
    print(f"Put  price: {put.price():.2f}")

    print(f"Call Δ: {call.delta():.2f}")
    print(f"Put  Δ: {put.delta():.2f}")

    print(f"Vega  : {call.vega():.2f}")

    print(f"Call ρ: {call.rho():.2f}")
    print(f"Put  ρ: {put.rho():.2f}")

    print(f"Call θ per year: {call.theta():.2f}; θ/day: {call.theta_per_day():.2f}")
    print(f"Put  θ per year: {put.theta():.2f}; θ/day: {put.theta_per_day():.2f}")

    # Put-Call parity (q=0): C - P = S - K e^{-rT}
    lhs = call.price() - put.price()
    rhs = call.S - call.K * math.exp(-call.r * call.T)
    print(f"Put-Call parity -> LHS: {lhs:.2f}, RHS: {rhs:.2f}")
