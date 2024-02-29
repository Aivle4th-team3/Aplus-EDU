function todayEvalsChartBuilder(canvas, num_correct, num_wrong) {
    const rate_correct = (num_correct / (num_correct + num_wrong)) * 100;
    const rate_wrong = (num_wrong / (num_correct + num_wrong)) * 100;

    new Chart(canvas, {
        type: "bar",
        data: {
            labels: ["오늘의 평가"],
            datasets: [
                {
                    label: "정답",
                    data: [rate_correct],
                    backgroundColor: "#6464ff",
                },
                {
                    label: "오답",
                    data: [rate_wrong],
                    backgroundColor: "rgba(255, 99, 132, 0.2)",
                },
            ],
        },
        options: {
            indexAxis: "y",
            plugins: {},
            maintainAspectRatio: false,
            responsive: true,
            scales: {
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true,
                },
            },
        },
    });
}
