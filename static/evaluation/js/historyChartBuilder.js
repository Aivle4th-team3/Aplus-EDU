function historyChartBuilder(canvas, history_evals) {
    labels = history_evals.map(({ score, evaluation_date }) => evaluation_date);
    data = history_evals.map(({ score, evaluation_date }) => score);

    new Chart(canvas, {
        type: "line",
        data: {
            labels,
            datasets: [
                {
                    label: "정답률",
                    data,
                    backgroundColor: "rgba(255, 99, 132, 0.2)",
                    borderColor: "rgba(255, 99, 132, 1)",
                    borderWidth: 2,
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {},
            interaction: {
                mode: "index",
                intersect: false,
            },
            scales: {
                x: {
                    display: true,
                    title: {
                        display: true,
                        text: "시간",
                    },
                },
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: "정답률",
                    },
                    suggestedMin: 0,
                    suggestedMax: 100,
                },
            },
        },
    });
}
