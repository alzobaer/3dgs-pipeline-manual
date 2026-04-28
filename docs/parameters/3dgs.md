# 3DGS Parameters

Optimal training settings.

## Key Parameters

```bash
--iterations 30000  # Full convergence
--resolution -1  # Use full resolution (4K)
```

## Memory Configuration

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

Prevents OOM fragmentation.
