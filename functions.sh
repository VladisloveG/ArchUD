umount_partitions() {
  mounted_partitions=($(lsblk | grep ${MOUNTPOINT} | awk '{print $7}' | sort -r))
  swapoff -a
  for i in ${mounted_partitions[@]}; do
    umount $i
  done
}