# Thuật toán Tiến hóa vi phân
class DifferentialEvolution:
    def __init__(self, objective_function, dimensions, bounds, population_size, mutation_factor, crossover_probability, generations):
        self.objective_function = objective_function
        self.dimensions = dimensions
        self.bounds = bounds
        self.population_size = population_size
        self.mutation_factor = mutation_factor
        self.crossover_probability = crossover_probability
        self.generations = generations
        self.best_solution = None
        self.best_value = float('inf')
        self.history = []  # Lưu giá trị tốt nhất của mỗi thế hệ
        self.population = None

    # Khởi tạo quần thể
    def initialize_population(self):
        return np.random.uniform(self.bounds[0], self.bounds[1], (self.population_size, self.dimensions))

    # Hàm đột biến
    def mutate(self, population, idx):
        indices = [i for i in range(self.population_size) if i != idx]
        a, b, c = np.random.choice(indices, 3, replace=False)
        mutant_vector = np.clip(population[a] + self.mutation_factor * (population[b] - population[c]), self.bounds[0], self.bounds[1])
        return mutant_vector

    # Hàm lai ghép
    def crossover(self, target_vector, mutant_vector):
        crossover_mask = np.random.rand(self.dimensions) < self.crossover_probability
        trial_vector = np.where(crossover_mask, mutant_vector, target_vector)
        return trial_vector
    
    # Hàm chọn lọc
    def select(self, population, trial_vector, idx):
        if self.objective_function.evaluate(trial_vector) < self.objective_function.evaluate(population[idx]):
            population[idx] = trial_vector
            value = self.objective_function.evaluate(population[idx])
            if value < self.best_value:
                self.best_value = value
                self.best_solution = population[idx]

    # Hàm thực thi
    def run(self):
        self.population = self.initialize_population()
        
        for generation in range(self.generations):
            for idx in range(self.population_size):
                mutant_vector = self.mutate(self.population, idx)
                trial_vector = self.crossover(self.population[idx], mutant_vector)
                self.select(self.population, trial_vector, idx)
            self.history.append(self.best_value)
            
        return self.best_solution, self.best_value