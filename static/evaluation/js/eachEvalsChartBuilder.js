function eachEvalsChartBuilder(canvas, detail_evals) {
    var eachScores = detail_evals.map(({ score, detail }) => ({ label: "", data: [score], backgroundColor: "#FEBE98" }));

    new Chart(canvas, {
        type: "bar",
        data: {
            labels: [""],
            datasets: eachScores,
        },
        options: {
            plugins: {},
            legend: {
                display: false,
            },
            maintainAspectRatio: false,
            responsive: true,
            scales: {
                y: {
                    display: true,
                    title: {
                        display: true,
                        text: "개별 정답퍼센트",
                    },
                    suggestedMin: 0,
                    suggestedMax: 100,
                },
            },
        },
    });
}
