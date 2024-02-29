function personalChartBuilder(canvas, grouped_scores) {
    const datasets = Object.entries(grouped_scores).map(([label, data]) => ({ label, data }));

    const l = Math.max(...datasets.map(({ label, data }) => data.length));
    const labels = Array(l).fill("");

    new Chart(canvas, {
        type: "line",
        data: {
            labels,
            datasets,
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
